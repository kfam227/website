param([int]$Port = 8080)
$root = Join-Path $PSScriptRoot "HTML"
$listener = [System.Net.HttpListener]::new()
$listener.Prefixes.Add("http://localhost:$Port/")
$listener.Start()
Write-Host "Serving $root on http://localhost:$Port/"
$mimeTypes = @{ ".html" = "text/html"; ".css" = "text/css"; ".js" = "application/javascript"; ".png" = "image/png"; ".jpg" = "image/jpeg"; ".svg" = "image/svg+xml" }
while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $req = $ctx.Request
    $res = $ctx.Response
    $local = $req.Url.LocalPath.TrimStart('/')
    $path = Join-Path $root $local
    if ($local -eq "" -or $local -eq "/") {
        $files = Get-ChildItem $root -Filter "*.html" | ForEach-Object { "<li><a href='/$($_.Name)'>$($_.Name)</a></li>" }
        $html = [System.Text.Encoding]::UTF8.GetBytes("<html><body><h2>HTML Docs</h2><ul>$($files -join '')</ul></body></html>")
        $res.ContentType = "text/html"; $res.ContentLength64 = $html.Length
        $res.OutputStream.Write($html, 0, $html.Length)
    } elseif (Test-Path $path -PathType Leaf) {
        $ext = [System.IO.Path]::GetExtension($path)
        $bytes = [System.IO.File]::ReadAllBytes($path)
        $res.ContentType = if ($mimeTypes[$ext]) { $mimeTypes[$ext] } else { "application/octet-stream" }
        $res.ContentLength64 = $bytes.Length
        $res.OutputStream.Write($bytes, 0, $bytes.Length)
    } else {
        $res.StatusCode = 404
    }
    $res.Close()
}
