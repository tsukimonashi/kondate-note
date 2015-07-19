% rebase('base.tpl')
<h4>献立の新規登録</h4>
<form action="/menus/new" method="POST">
    <div class="form-group">
        <label>名前</label>
        <input class="form-control" type="text" name="name">
    </div>
    <div class="form-group">
        <label>カロリー</label>
        <input class="form-control" type="number" name="kcal">
    </div>
    <div class="form-group">
        <label>画像URL</label>
        <input class="form-control" type="text" name="image">
    </div>
    <button class="btn btn-primary" type="submit">送信</button>
</form>
