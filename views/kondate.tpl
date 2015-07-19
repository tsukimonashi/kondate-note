% rebase('base.tpl')
<h3>献立の一覧</h3>
<ul class="list-group">
    % for menu in menus:
    <li class="list-group-item">
        {{menu['name']}} {{menu['kcal']}}
        <img src="{{menu['image']}}">
    </li>
    % end
</ul>
