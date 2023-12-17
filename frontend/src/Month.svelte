<script>
    import {
        startOfMonth,
        endOfMonth,
        eachDayOfInterval,
        format,
    } from "date-fns";

    // Get the current date and determine the start and end of the month
    const today = new Date();
    const firstDayOfMonth = startOfMonth(today);
    const lastDayOfMonth = endOfMonth(today);

    // Get all days in the month
    let daysInMonth = eachDayOfInterval({
        start: firstDayOfMonth,
        end: lastDayOfMonth,
    });

    // Format the days to start from Monday
    const startWeekday = firstDayOfMonth.getDay();
    const daysToPad = startWeekday === 0 ? 6 : startWeekday - 1;
    const paddedDays = new Array(daysToPad).fill(null).concat(daysInMonth);

    // Add additional padding to make the array length a multiple of 7
    while (paddedDays.length % 7 !== 0) {
        paddedDays.push(null);
    }

    // Utility function to format the date
    const formatDate = (date) => (date ? format(date, "d") : "");
</script>

<div class="grid">
    {#each paddedDays as day}
        <div class="day {day === null ? 'non-month-day' : ''}">
            {formatDate(day)}
        </div>
    {/each}
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-gap: 10px;
    }
    .day {
        padding: 10px;
        text-align: center;
        background-color: #f0f0f0;
    }
    .non-month-day {
        background-color: #e0e0e0;
    }
</style>
