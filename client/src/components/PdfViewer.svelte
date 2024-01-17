<script lang="ts">
    import { onMount, onDestroy } from 'svelte';
    import * as pdfjs from 'pdfjs-dist';

    pdfjs.GlobalWorkerOptions.workerSrc =
        'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.5.141/pdf.worker.min.js';

    export let url = '';
    let canvasContainer: HTMLDivElement;

    async function renderPage(page: pdfjs.PDFPageProxy) {
        const viewport = page.getViewport({ scale: 1.2 });

        const wrapper = document.createElement('div');
        wrapper.className = 'mb-4 relative bg-white rounded-lg shadow overflow-hidden';
        wrapper.id = `page-${page._pageIndex + 1}`;
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');

        if (!ctx) {
            return;
        }

        canvas.height = viewport.height;
        canvas.width = viewport.width;
        wrapper.appendChild(canvas);
        canvasContainer.appendChild(wrapper);

        page.render({
            canvasContext: ctx,
            viewport: viewport
        });

        const textLayer = document.createElement('div');
        textLayer.className = 'textLayer absolute top-0 left-0 w-full h-full';
        const textContent = await page.getTextContent();
        pdfjs.renderTextLayer({
            textContentSource: textContent,
            viewport: page.getViewport(),
            container: textLayer
        });

        wrapper.appendChild(textLayer);
    }

    let destroyed = false;
    onMount(async () => {
        const pdfDoc = await pdfjs.getDocument(url).promise;

        if (destroyed) {
            return;
        }

        for (let num = 1; num <= pdfDoc.numPages; num++) {
            pdfDoc.getPage(num).then(renderPage);
        }
    });

    onDestroy(() => {
        destroyed = true;
    });
</script>

<div class="pdf-container">
    <div bind:this={canvasContainer} class="pdf-wrapper" />
</div>

<style>
    .pdf-container {
        height: calc(100vh - 80px);
    }
    .pdf-wrapper {
        flex: 1;
        background: #f3f4f6; /* Tailwind's light gray */
        padding: 16px;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow-y: auto;
        max-height: 100%;
    }
</style>
