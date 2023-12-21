<!-- HabitModal.svelte -->
<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher();
    export let selectedDate;
    export let habitsData = [];
    export let selectedDateData = [];

    let habitsWithState = habitsData.map((habitData) => {
        return {
            ...habitData,
            state: selectedDateData.some(
                (entry) => entry.habit_id === habitData.id,
            ),
        };
    });

    async function setHabit(habitId) {
        const habitIndex = habitsWithState.findIndex((h) => h.id === habitId);
        if (habitIndex !== -1) {
            habitsWithState[habitIndex].state =
                !habitsWithState[habitIndex].state;
            const response = await fetch(
                "http://localhost:9922/upsert_days_habits",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        habit_id: habitId,
                        date: selectedDate,
                        state: habitsWithState[habitIndex].state,
                    }),
                },
            );

            if (response.ok) {

                dispatch("habitsUpdated");
            } else {
                // If the update fails, revert the state change in the array
                habitsWithState[habitIndex].state =
                    !habitsWithState[habitIndex].state;
                console.error("Error updating habit entry", response.status);
            }
        }
    }

    function closeModal() {
        dispatch("closeModal");
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="modal-background" on:click={closeModal}>
    <div class="modal-content" on:click|stopPropagation>
        <div>
            {selectedDate}
        </div>

        {#each habitsWithState as habit}
            <div
                class="habit-entry"
                on:click={() => setHabit(habit.id)}
                style="background-color: {habit.state
                    ? habit.display_colour
                    : '#b5b5b5'}"
            >
                {habit.name}
            </div>
        {/each}
    </div>
</div>

<style>
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 10;
    }
    .modal-content {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .habit-entry {
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        cursor: pointer;
    }
</style>
