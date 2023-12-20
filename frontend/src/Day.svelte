<script>
    export let daysData;
    export let dayNumber;
</script>

<div class="day-container">
    <div class="day-number-display">
        {dayNumber}
    </div>

    <div class="habit-grid">
        {#each daysData as habit}
            <div
                class="habit-cell"
                style="background-color: {habit.displayColor}"
                title={habit.habitDescription}
            >
                {habit.habitName}{habit.value ? ` ${habit.value}` : ""}
            </div>
        {/each}
    </div>
</div>

<style>
    .day-container {
        position: relative;
        display: flex;
        flex-direction: column; /* Changed to column for vertical list */
        align-items: center;
        height: 100%;
        border: 1px rgb(25, 25, 25) solid;
        cursor: pointer;
    }

    .day-container:hover{
        border: white 1px solid;
        z-index: 2;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.4);
        background-color: #252525;
    }

    .day-number-display {
        position: absolute;
        top: 5px; /* Align the day number to the top */
        left: 5px;
        font-size: 1rem; /* Adjusted for better fit */
        color: rgb(60, 60, 60);
        z-index: 1;
    }

    .habit-grid {
        display: flex;
        flex-direction: column; /* Changed to column for vertical list */
        align-items: center;
        z-index: 0;
        width: 100%;
    }

    .habit-cell {
        color: white;
        width: 100%;
        text-align: center;
        font-size: 0.8rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
