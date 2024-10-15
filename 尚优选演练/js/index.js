window.onload = function () {
    // 获取元素
    var navPath = document.querySelector('.wrapper #content .contentMain #navPath');
    var path = goodData.path;

    for (var i = 0; i < path.length; i++) {
        if (i == path.length - 1) {
            var a = document.createElement('a');
            a.innerText = path[i].title;
            navPath.appendChild(a);
        } else {
            var a = document.createElement('a');
            var s = document.createElement('i');
            a.innerText = path[i].title;
            a.href = path[i].url;
            s.innerText = '/';
            navPath.appendChild(a);
            navPath.appendChild(s);
        }
    }
}