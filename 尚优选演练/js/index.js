window.onload = function () {
    navPathDataBind()
    function navPathDataBind() {
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

        // 放大镜效果
        bigGlassBind()
        function bigGlassBind() {
            /**
             * 思路：
             * 1、获取小图框元素对象，并且设置移入事件(onMouseenter)
             * 2、动态创建蒙版元素以及大图框和大图片元素
             * 3、移出时需要移除蒙版元素和大图框及图片
             */
            // 获取小图框元素
            const smallPic = document.querySelector('#smallPic');
            const leftTop = document.querySelector('#leftTop')
            // 设置移入事件
            // smallPic.addEventListener('mouseenter', fun)
            // console.log(smallPic)
            smallPic.onmouseenter = function () {
                // 创建蒙版元素
                const maskDiv = document.createElement('div');
                maskDiv.className = 'mask';
                // 创建大图框元素
                const bigPic = document.createElement('div');
                bigPic.id = 'bigPic';
                // 创建大图片元素
                const bigImg = document.createElement('img')
                bigImg.src = 'images/b1.png';
                bigPic.appendChild(bigImg);
                smallPic.appendChild(maskDiv);
                leftTop.appendChild(bigPic);
                // 设置移动效果
                smallPic.onmousemove = function (event) {
                    let left = event.clientX - smallPic.getBoundingClientRect().left - maskDiv.offsetWidth / 2;
                    let top = event.clientY - smallPic.getBoundingClientRect().top - maskDiv.offsetHeight / 2;
                    // 判断
                    if (left < 0) {
                        left = 0
                    } else if (left > smallPic.offsetWidth - maskDiv.offsetWidth) {
                        left = smallPic.offsetWidth - maskDiv.offsetWidth
                    }

                    if (top < 0) {
                        top = 0
                    } else if (top > smallPic.offsetHeight - maskDiv.offsetHeight) {
                        top = smallPic.offsetHeight - maskDiv.offsetHeight
                    }
                    maskDiv.style.left = left + 'px';
                    maskDiv.style.top = top + 'px';
                    // 控制大图移动
                    let scale = (smallPic.clientWidth - maskDiv.offsetWidth) / (bigImg.offsetWidth - bigPic.clientWidth);
                    console.log(scale)
                    bigImg.style.left = -left / scale + 'px';
                    bigImg.style.top = -top / scale + 'px';
                }
                // 设置移除效果
                smallPic.onmouseleave = function () {
                    smallPic.removeChild(maskDiv)
                    leftTop.removeChild(bigPic)
                }
            }
        }

    }


}