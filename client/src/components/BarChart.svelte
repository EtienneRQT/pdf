<script lang="ts">
    import { onMount } from 'svelte';
    import Chart from 'chart.js/auto';

    export let data: { [key: string]: number[] };
    export let startingColor: { r: number; g: number; b: number };

    let chartCanvas: HTMLCanvasElement;

    onMount(() => {
        const ctx = chartCanvas.getContext('2d');
        if (!ctx) {
            return;
        }

        const labels = Object.keys(data);
        const chartValues = Object.values(data).map(
            (scores) => scores.reduce((a, b) => a + b, 0) / scores.length
        );

        new Chart(ctx, {
            type: 'bar',
            options: {
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        min: -1,
                        max: 1,
                        grid: {
                            lineWidth: ({ tick }) => (tick.value == 0 ? 2 : 1),
                            color: ({ tick }) => (tick.value === 0 ? 'rgba(0, 0, 0, 0.7)' : 'rgba(0, 0, 0, 0.1)')
                        },
                        ticks: {
                            stepSize: 0.33,
                            font: {
                                size: 15
                            }
                        }
                    },
                    x: {
                        ticks: {
                            font: {
                                size: 20
                            }
                        }
                    }
                }
            },
            data: {
                labels: labels,
                datasets: [
                    {
                        base: 0,
                        label: '',
                        data: chartValues,
                        backgroundColor: generateColors(startingColor, 7, 0.2),
                        borderColor: generateColors(startingColor, 7),
                        borderWidth: 1
                    }
                ]
            }
        });
    });

    // Functions for color generation remain the same
</script>

<canvas
    bind:this={chartCanvas}
    class="shadow-xl rounded-lg overflow-hidden"
/>
