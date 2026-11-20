# Automated Runner for GreenInfer
# Make sure Ollama is running before starting this script.

Write-Host "==========================================================" -ForegroundColor Green
Write-Host " Starting GreenInfer Automated Benchmark Suite" -ForegroundColor Green
Write-Host " Target Hardware: AMD Ryzen 5 5500U (16GB RAM, Windows 11)" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green

$models = @("qwen2.5:0.5b", "qwen2.5:1.5b", "llama3.2:3b", "phi3.5:latest", "mistral:7b")
$tasks = @("classification", "qa", "summarization", "code")

# Test 1 sample first to verify pipeline
Write-Host "`n[*] Verifying Ollama API is reachable..." -ForegroundColor Yellow
try {
    $res = Invoke-RestMethod -Uri "http://localhost:11434/api/tags" -Method Get
    Write-Host "[+] Ollama is online! Available models: $($res.models.name -join ', ')" -ForegroundColor Cyan
} catch {
    Write-Host "[!] ERROR: Ollama is not running! Please start Ollama or run 'ollama serve' in another terminal." -ForegroundColor Red
    exit
}

# Run sequential benchmarks (3 trials per configuration)
foreach ($model in $models) {
    Write-Host "`n>>> Processing Model: $model" -ForegroundColor Magenta
    foreach ($task in $tasks) {
        for ($trial = 1; $trial -le 3; $trial++) {
            Write-Host "--- Running Model: $model | Task: $task | Trial: #$trial ---" -ForegroundColor Gray
            python benchmark.py --model $model --task $task --samples 50 --trial $trial
            Start-Sleep -Seconds 3 # Cooling pause between runs to avoid thermal throttling
        }
    }
}

Write-Host "`n[*] Generating plots and LaTeX tables..." -ForegroundColor Green
python analyze.py

Write-Host "`n[✓] ALL EXPERIMENTS COMPLETE! Check the results/ and results/figures/ directories." -ForegroundColor Green
