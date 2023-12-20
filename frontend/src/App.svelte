<script>
	import { onMount } from "svelte";
	import Month from "./Month.svelte";

	let habitsData = [];
	let dataLoaded = false; // State to track if data is loaded

	onMount(async () => {
		const response = await fetch("http://localhost:9922/habits");
		if (response.ok) {
			const data = await response.json();
			habitsData = data.habits;
			dataLoaded = true;
		} else {
			console.error("Error fetching habit list", response.status);
		}
	});
</script>

<main>
	{#if dataLoaded}
		<Month {habitsData} />
	{:else}
		<p>Loading...</p>
	{/if}
</main>

<style>
	main {
		text-align: center;
		max-width: 240px;
		margin: 0 auto;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
