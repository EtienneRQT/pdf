<script lang="ts">
	export let label: string = '';
</script>

<div class="bg-white shadow-md rounded-lg p-4 hover:shadow-lg transition-shadow duration-300">
	<div class="flex justify-between items-center">
		<label for="" class="block text-lg font-semibold text-gray-700 mb-2">{label}</label>
	</div>
	<div class="relative">
		<slot />
	</div>
</div>
