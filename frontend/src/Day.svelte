<script>
    export let daysData; 
    export let dayNumber = 0;
</script>

<div class="day-container">
    <div class="day-number-display">
        {dayNumber}
    </div>

    <div class="habit-grid">
        {#each daysData as habit}
            <div class="habit-cell" style="background-color: {habit.displayColor}" title="{habit.habitDescription}">
                {habit.habitName}{habit.value ? ` ${habit.value}` : ''}
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
    }

    .day-number-display {
        position: absolute;
        top: 0; /* Align the day number to the top */
        font-size: 2rem; /* Adjusted for better fit */
        color: rgba(0, 0, 0, 0.1);
        z-index: 1;
    }

    .habit-grid {
        display: flex;
        flex-direction: column; /* Changed to column for vertical list */
        align-items: center;
        gap: 4px; /* Gap between each habit cell */
        padding: 10px;
        z-index: 0;
    }

    .habit-cell {
        min-width: 100px; /* Adjust width for better readability */
        padding: 5px;
        border-radius: 4px; /* Optional for rounded corners */
        border: 1px solid transparent; /* Transparent border for consistent sizing */
        text-align: center;
        font-size: 0.8rem;
        cursor: pointer; /* Indicates that the item is interactive */
    }
</style>
