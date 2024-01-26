<script>
	import { tweened } from 'svelte/motion';

	export let progress = 0;

	const width = tweened(1, {
		duration: 1000
	});

	$: width.set(progress);
</script>

{#if $$slots.default && $width === 100}
	<slot />
{:else}
	<div class="flex my-4 w-full h-2.5 bg-gray-200 rounded-full overflow-hidden shadow-inner dark:bg-gray-700">
		<div
			class="flex flex-col justify-center bg-gradient-to-r from-blue-500 to-purple-600 transition-all duration-500 ease-in-out"
			role="progressbar"
			style="width: {$width}%"
		/>
	</div>
{/if}
