<!DOCTYPE html>
<html lang="en">
<head>
  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-K27QLF3HX0"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
  
    gtag('config', 'G-K27QLF3HX0');
  </script>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🧬 VirTransformer – Predict Pathogenicity</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap" rel="stylesheet">
  <style>
    body {
      font-family: 'Inter', sans-serif;
      background: #f0f4f8;
      padding: 2rem;
      color: #333;
    }

    .container {
      max-width: 880px;
      margin: auto;
      background: white;
      border-radius: 16px;
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
      padding: 2.5rem;
    }

    h1 {
      text-align: center;
      font-size: 2.2rem;
      background: linear-gradient(to right, #1a73e8, #4caf50);
      -webkit-background-clip: text;
      color: transparent;
      margin-bottom: 1rem;
    }

    p.description {
      text-align: center;
      color: #666;
      margin-bottom: 2rem;
    }

    .radio-options {
      text-align: center;
      margin-bottom: 1rem;
    }

    .radio-options label {
      margin: 0 1.5rem;
      font-size: 1rem;
      cursor: pointer;
    }

    textarea {
      width: 100%;
      font-size: 1rem;
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 10px;
      margin-bottom: 1.5rem;
      background: #f9f9f9;
    }

    button {
      width: 100%;
      padding: 1rem;
      background: #1a73e8;
      color: white;
      font-size: 1.05rem;
      font-weight: bold;
      border: none;
      border-radius: 10px;
      cursor: pointer;
    }

    button:hover {
      background: #0d47a1;
    }

    .output-box {
      margin-top: 2rem;
      padding: 1.5rem;
      border-radius: 12px;
      background: #e8f5e9;
      display: none;
    }

    .output-line {
      font-size: 1rem;
      margin-bottom: 0.5rem;
      padding-left: 1rem;
    }

    .spinner {
      margin: 20px auto;
      width: 40px;
      height: 40px;
      border: 5px solid rgba(0, 0, 255, 0.2);
      border-left-color: #1a73e8;
      border-radius: 50%;
      animation: spin 1s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    footer {
      text-align: center;
      margin-top: 3rem;
      font-size: 0.9rem;
      color: #777;
    }

    footer a {
      color: #1a73e8;
      text-decoration: none;
    }

    footer a:hover {
      text-decoration: underline;
    }

    /* ========== Cite Box Styles ========== */
    .cite-box {
      max-width: 880px;
      margin: 2.5rem auto;
      padding: 1.5rem 2rem;
      background: linear-gradient(to right, #1a73e8, #4caf50);
      border-radius: 16px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.15);
      font-family: 'Inter', sans-serif;
      color: white;
      animation: fadeIn 0.6s ease;
    }

    .cite-box h3 {
      font-size: 1.4rem;
      margin-bottom: 1rem;
      font-weight: 700;
      text-align: center;
    }

    .cite-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1rem;
    }

    .cite-content p {
      font-size: 1rem;
      line-height: 1.6;
      text-align: center;
    }

    .cite-content a {
      font-weight: 600;
      color: #fff;
      text-decoration: underline;
    }

    .cite-content a:hover {
      opacity: 0.9;
    }

    .cite-content button {
      background: #fff;
      border: none;
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      color: #1a73e8;
      font-weight: bold;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .cite-content button:hover {
      background: #e8f5e9;
      color: #0d47a1;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>

<div class="container">
  <h1>🧬 VirTransformer</h1>
  <p class="description">AI tool to predict human pathogenicity from viral DNA/RNA sequence or NCBI Accession ID (More than 95% Accurate)</p>

  <div class="radio-options">
    <label><input type="radio" name="inputType" value="sequence" checked> Viral Sequence</label>
    <label><input type="radio" name="inputType" value="accession"> Accession ID</label>
  </div>

  <textarea id="dnaInput" placeholder="Paste DNA Sequence or Accession ID..."></textarea>
  <button onclick="predict()">🚀 Run Prediction</button>

  <!-- Spinner -->
  <div class="spinner" id="spinner" style="display: none;"></div>
  
  <!-- Output Display -->
  <div class="output-box" id="outputBox">
    <p class="output-line" id="labelLine">🧬 Label: —</p>
    <p class="output-line" id="scoreLine">📊 Confidence Score: —</p>
    <p class="output-line" id="accessionLine">🧾 Input/Accession: —</p>
  </div>
</div>


<script>
  async function predict() {
    const seq = document.getElementById("dnaInput").value.trim();
    const inputType = document.querySelector('input[name="inputType"]:checked').value;
    const spinner = document.getElementById("spinner");
    const outputBox = document.getElementById("outputBox");

    const labelLine = document.getElementById("labelLine");
    const scoreLine = document.getElementById("scoreLine");
    const accessionLine = document.getElementById("accessionLine");

    if (!seq) {
      alert("⚠️ Please enter a sequence or accession ID.");
      return;
    }

    outputBox.style.display = "none";
    spinner.style.display = "block";

    let endpoint = inputType === "sequence" ? "/predict_sequence" : "/predict_accession";

    try {
      const res = await fetch("https://vhbert.onrender.com" + endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ seq: seq })
      });

      if (!res.ok) {
        alert(`❌ Server Error ${res.status}`);
        spinner.style.display = "none";
        return;
      }

      const data = await res.json();
      spinner.style.display = "none";

      labelLine.textContent = `🧬 Label: ${data.result.label_name || "Unknown"}`;
      scoreLine.textContent = `📊 Confidence Score: ${data.result.confidence?.toFixed(4) || "—"}`;
      accessionLine.textContent = `🧾 Input/Accession: ${data.accession || "Sequence"}`;

      outputBox.style.display = "block";
      renderGenome(data.result.chunks, data.result.genome_length, data.result.annotations_gff);
    } catch (error) {
      alert("❌ Network error: " + error.message);
      spinner.style.display = "none";
    }
  }

  async function copyCitation() {
    const citation = `Decoding the Genomic Landscape of Viruses Using Deep Learning: An Integrated Analysis
R Atif, IIUI, 2024
Google Scholar: https://scholar.google.com/citations?view_op=view_citation&hl=en&user=a4fOyR8AAAAJ&citation_for_view=a4fOyR8AAAAJ:d1gkVwhDpl0C`;

    try {
      await navigator.clipboard.writeText(citation);
      const btn = document.getElementById("copyBtn");
      btn.textContent = "✅ Copied!";
      setTimeout(() => btn.textContent = "📋 Copy", 2000);
    } catch (err) {
      alert("❌ Failed to copy: " + err);
    }
  }
</script>


<!-- Genome Pathogenicity Box -->
<div class="genome-box">
  <h2>🧬 Genome Pathogenicity View</h2>
  <div id="igv-container" style="width:100%; height:500px; background:white; border-radius:12px;"></div>
</div>

<!-- IGV.js -->
<script src="https://cdn.jsdelivr.net/npm/igv/dist/igv.min.js"></script>

<style>
  .genome-box {
    max-width: 880px;
    margin: 2.5rem auto;
    padding: 1.5rem;
    background: linear-gradient(to right, #1a73e8, #4caf50);
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    font-family: 'Inter', sans-serif;
    color: white;
    animation: fadeIn 0.6s ease;
  }
  .genome-box h2 {
    text-align: center;
    margin-bottom: 1rem;
    font-size: 1.4rem;
  }
</style>

<script>
  let igvBrowser = null;

  async function renderGenome(predChunks, genomeLength, gffData) {
    // === 1. Remove old browser if exists ===
    if (igvBrowser) {
      igv.removeBrowser(igvBrowser);
      igvBrowser = null;
    }

    // === 2. BED track for labels (red/green) ===
    let bed = "";
    predChunks.forEach(chunk => {
      const label = chunk.label.toLowerCase() === "pathogenic" ? "pathogenic" : "nonpathogenic";
      bed += `virus\t${chunk.start}\t${chunk.end}\t.\t${chunk.score}\n`;
    });

    // === 3. BedGraph track for probabilities (per-base) ===
    let bedGraph = "track type=bedGraph name=\"PredictionScores\"\n";
    predChunks.forEach(chunk => {
      for (let pos = chunk.start; pos < chunk.end; pos++) {
        bedGraph += `virus\t${pos}\t${pos+1}\t${chunk.score}\n`;
      }
    });

    // === 4. Create object URLs ===
    const bedUrl = URL.createObjectURL(new Blob([bed], { type: "text/plain" }));
    const bedGraphUrl = URL.createObjectURL(new Blob([bedGraph], { type: "text/plain" }));
    const gffUrl = URL.createObjectURL(new Blob([gffData], { type: "text/plain" }));
    const fastaUrl = URL.createObjectURL(new Blob([`>virus\n${"N".repeat(genomeLength)}`], { type: "text/plain" }));

    // === 5. IGV config ===
    const options = {
      reference: {
        id: "virus",
        name: "Virus Genome",
        fastaURL: fastaUrl
      },
      tracks: [
        {
          name: "Genome Annotations",
          type: "annotation",
          format: "gff3",
          url: gffUrl,
          displayMode: "EXPANDED"
        },
        {
          name: "Pathogenicity Predictions",
          type: "annotation",
          format: "bed",
          url: bedUrl,
          color: feature => feature.score > 0.5 ? "red" : "green",
          displayMode: "EXPANDED"
        },
        {
          name: "Prediction Scores (Wave)",
          type: "wig",
          format: "bedgraph",
          url: bedGraphUrl,
          color: "blue",
          autoscale: true,
          min: 0,
          max: 1,
          displayMode: "EXPANDED"
        }
      ]
    };

    // === 6. Create browser ===
    const igvDiv = document.getElementById("igv-container");
    igvDiv.innerHTML = "";
    igvBrowser = await igv.createBrowser(igvDiv, options);
    console.log("New IGV browser created");
  }
</script>

<!-- ===================== Cite Us Box ===================== -->
<div class="cite-box">
  <h3>📖 Cite us</h3>
  <div class="cite-content">
    <p>
      <strong>Decoding the Genomic Landscape of Viruses Using Deep Learning: An Integrated Analysis</strong><br>
      <span class="author">R Atif</span>, <span class="affiliation">IIUI</span>, <span class="year">2024</span><br>
      <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=a4fOyR8AAAAJ&citation_for_view=a4fOyR8AAAAJ:d1gkVwhDpl0C" target="_blank">
        Google Scholar Link
      </a>
    </p>
    <button id="copyBtn" onclick="copyCitation()">📋 Copy</button>
  </div>
</div>

<footer>
  Built with ❤️ by <a href="https://bioaml.org" target="_blank">BioAML</a>
</footer>  
</body>
</html>
