<script lang="ts">
	export let type: string = 'text';
	export let value = '';

	function typeAction(node: HTMLInputElement) {
		node.type = type;
	}
</script>

<input
	use:typeAction
	bind:value
	class="py-2 px-3 block w-full border-2 border-gray-300 rounded-lg text-sm focus:border-blue-600 focus:ring-2 focus:ring-blue-500 focus:outline-none transition duration-200 ease-in-out shadow-sm hover:shadow-md"
	required
/>
