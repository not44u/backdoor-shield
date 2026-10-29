document.querySelector('.center').addEventListener('mousemove', function (e) {
    const ball = this.querySelector('::before'); // 获取光球
    const center = this.getBoundingClientRect(); // 获取.center元素的边界
    const x = e.clientX - center.left; // 获取鼠标相对于.center的水平位置
    const y = e.clientY - center.top;  // 获取鼠标相对于.center的垂直位置

    // 设置光球的渐变颜色，渐变基于鼠标相对位置
    const gradient = `linear-gradient(
        45deg, 
        rgba(${Math.floor((x / center.width) * 255)}, 0, 0, 0.7), 
        rgba(0, ${Math.floor((y / center.height) * 255)}, 0, 0.7)
    )`;

    // 设置光球的位置和渐变背景
    this.style.setProperty('--ball-x', `${x}px`);
    this.style.setProperty('--ball-y', `${y}px`);
    ball.style.background = gradient; // 应用渐变效果
});
