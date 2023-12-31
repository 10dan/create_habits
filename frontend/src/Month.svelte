<script>
    import { onMount } from "svelte";
    import Day from "./Day.svelte";
    import HabitModal from "./HabitModal.svelte";
    import {
        startOfMonth,
        endOfMonth,
        eachDayOfInterval,
        format,
    } from "date-fns";

    export let habitsData;
    let thisMonthsDayData = [];
    let dataLoaded = false;
    let showModal = false;
    let selectedDate = null;
    let selectedDateData = null;

    function openModal(day) {
        selectedDate = formatDate(day);
        selectedDateData = getDayData(formatDate(day));
        showModal = true;
    }

    function closeModal() {
        showModal = false;
    }

    const today = new Date();
    const firstDayOfMonth = startOfMonth(today);
    const lastDayOfMonth = endOfMonth(today);
    let daysInMonth = eachDayOfInterval({
        start: firstDayOfMonth,
        end: lastDayOfMonth,
    });
    const startWeekday = firstDayOfMonth.getDay();
    const daysToPad = startWeekday === 0 ? 6 : startWeekday - 1;
    const paddedDays = new Array(daysToPad).fill(null).concat(daysInMonth);
    while (paddedDays.length % 7 !== 0) {
        paddedDays.push(null);
    }

    onMount(async () => {
        await getThisMonthsData();
    });

    async function getThisMonthsData() {
        const year = today.getFullYear();
        const month = today.getMonth() + 1; // getMonth() returns 0-11

        const response = await fetch(
            `http://localhost:9922/habits/${year}/${month}`,
        );
        if (response.ok) {
            const data = await response.json();
            thisMonthsDayData = data.habit_logs;
            dataLoaded = true;
        } else {
            console.error(
                `Error fetching logs for ${month}/${year}:`,
                response.status,
            );
        }
    }

    // Utility function to format the date
    const formatDate = (date) => (date ? format(date, "yyyy-MM-dd") : "");

    function getDayData(date) {
        const dayLogs = thisMonthsDayData.filter((log) => log.date === date);
        return dayLogs
            .map((log) => {
                const habit = habitsData.find((h) => h.id === log.habit_id);
                if (habit) {
                    return {
                        ...log,
                        habitName: habit.name,
                        habitDescription: habit.description,
                        displayColor: habit.display_colour,
                    };
                }
                return null;
            })
            .filter((item) => item !== null);
    }
</script>

{#if showModal}
    <HabitModal
        {habitsData}
        {selectedDateData}
        {selectedDate}
        on:closeModal={closeModal}
        on:habitSet={() => {
            getThisMonthsData();
        }}
    />
{/if}

<!-- svelte-ignore a11y-click-events-have-key-events -->
<div class="container">
    <div class="grid">
        {#if dataLoaded}
            {#each paddedDays as day}
                <div
                    class="day {day === null ? 'non-month-day' : ''}"
                    on:click={() => openModal(day)}
                >
                    {#if day}
                        <Day
                            daysData={getDayData(formatDate(day))}
                            dayNumber={day.getDate()}
                            {habitsData}
                        />
                    {/if}
                </div>
            {/each}
        {/if}
    </div>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        padding: 0;
    }
    .grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-auto-rows: minmax(10vh, auto);
        grid-gap: 0px;
        width: 60vw;
    }
    .day {
        padding: 0px;
        text-align: center;
        background-color: #131313;
    }
    .non-month-day {
        background-color: black;
    }
</style>
