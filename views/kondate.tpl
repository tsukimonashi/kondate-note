<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>献立</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
<div class="container">
    <h1>献立の一覧</h1>
    <ul>
    % for menu in menus:
        <li>{{menu['name']}} {{menu['kcal']}}</li>
    % end
    </ul>
</div>
</body>
</html>
