<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample Wikipedia Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Wikipedia</h1>
            <input type="search" placeholder="Search Wikipedia">
        </div>
    </header>

    <nav>
        <div class="container">
            <ul>
                <li><a href="#">Main Page</a></li>
                <li><a href="#">Contents</a></li>
                <li><a href="#">Current events</a></li>
                <li><a href="#">Random article</a></li>
                <li><a href="#">About Wikipedia</a></li>
                <li><a href="#">Contact us</a></li>
                <li><a href="#">Donate</a></li>
            </ul>
        </div>
    </nav>

    <main>
        <div class="container">
            <article>
                <h2>Sample Essay Title</h2>
                <p>
                    This is a sample essay paragraph. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum. Cras venenatis euismod malesuada.
                </p>
                <h3>Introduction</h3>
                <p>
                    This section introduces the topic. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam.
                </p>
                <h3>Body</h3>
                <p>
                    This is the main body of the essay. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec pretium mi. Curabitur facilisis ornare velit non vulputate.
                </p>
                <h3>Conclusion</h3>
                <p>
                    This is the conclusion. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam ultrices, sem ut sollicitudin ullamcorper, augue nunc vehicula risus, at facilisis purus lacus ut est.
                </p>
            </article>
        </div>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 Wikipedia Clone. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>




body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
}

.container {
    width: 80%;
    margin: 0 auto;
    overflow: hidden;
}

header {
    background: #333;
    color: #fff;
    padding-top: 30px;
    min-height: 70px;
    border-bottom: #0779e4 3px solid;
}

header h1 {
    float: left;
    margin-top: 0;
}

header input[type="search"] {
    float: right;
    margin-top: 10px;
    padding: 5px;
    font-size: 18px;
}

nav {
    background: #0779e4;
    color: #fff;
    padding: 15px 0;
}

nav ul {
    padding: 0;
    list-style: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

main {
    padding: 20px 0;
}

article {
    background: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
    margin-top: 20px;
}








