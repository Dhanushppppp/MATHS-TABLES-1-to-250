<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Multiplication Tables</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .table {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

<h1>Multiplication Tables (1 to 20)</h1>

<script>
    for (let num = 1; num <= 20; num++) {
        document.write("<div class='table'>");
        document.write("<h3>Table of " + num + "</h3>");
        for (let i = 1; i <= 10; i++) {
            document.write(num + " x " + i + " = " + (num * i) + "<br>");
        }
        document.write("</div>");
    }
</script>

</body>
</html>
