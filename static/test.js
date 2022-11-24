document.addEventListener('DOMContentLoaded', () => {
    const heads = document.querySelectorAll('h2');
    if (heads && heads.length) {
        let contents = '';
        heads.forEach((head, i) => {
            let className = '';
            switch(head.localName) {
                case "h1":
                    className = `contents1`;
                    break;
                case "h2":
                    className = `contents2`;
                    break;
                case "h3":
                    className = `contents3`;
                    break;
                case "h4":
                    className = `contents4`;
                    break;
                case "h5":
                    className = `contents5`;
                    break;
                case "h6":
                    className = `contents6`;
                    break;
            }
            contents += `<li><a class="${className}" href="#head${i}">${head.textContent}</a></li>`;
            head.innerHTML += `<a id="head${i}"></a>`;
        })
        document.querySelector('#table-of-content').innerHTML += `<ol>${contents}</ol>`;
    }
});