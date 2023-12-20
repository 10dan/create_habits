<!-- HabitModal.svelte -->
<script>
    import { createEventDispatcher } from 'svelte';
    export let habitsData;
    export let selectedDate;

    const dispatch = createEventDispatcher();

    async function setHabit(habitId) {
        const response = await fetch('/create_habit_entry', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ habit_id: habitId, date: selectedDate }),
        });

        if (response.ok) {
            dispatch('habitSet', { habitId });
        } else {
            console.error('Error creating habit entry', response.status);
        }
    }

    function closeModal() {
        dispatch('closeModal');
    }
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="modal-background" on:click={closeModal}>
    <div class="modal-content" on:click|stopPropagation>
        {#each habitsData as habit}
            <div class="habit-entry" on:click={() => setHabit(habit.id)}>
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
