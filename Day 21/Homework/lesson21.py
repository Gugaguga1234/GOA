<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Semantic HTML Example</title>
</head>
<body>
    <!-- The header section typically contains the logo, site title, and navigation links -->
    <header>
        <h1>My Website</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- The main section contains the primary content of the webpage -->
    <main>
        <section id="home">
            <h2>Welcome to My Website</h2>
            <p>This is the home section of the website.</p>
            <!-- Embedding a video in the main content -->
            <video controls>
                <source src="sample-video.mp4" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>Learn more about us in this section.</p>
            <!-- Embedding an audio file in the main content -->
            <audio controls>
                <source src="sample-audio.mp3" type="audio/mp3">
                Your browser does not support the audio element.
            </audio>
        </section>

        <section id="contact">
            <h2>Contact Information</h2>
            <p>Get in touch with us through the contact information provided here.</p>
            <!-- Creating a table to display contact information -->
            <table border="1">
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                </tr>
                <tr>
                    <td>John Doe</td>
                    <td>john@example.com</td>
                    <td>123-456-7890</td>
                </tr>
                <tr>
                    <td>Jane Smith</td>
                    <td>jane@example.com</td>
                    <td>098-765-4321</td>
                </tr>
            </table>
        </section>
    </main>

    <!-- The footer section contains the website's footer information -->
    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>
</body>
</html>
