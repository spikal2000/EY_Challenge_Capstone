
<?php
    $db = new mysqli("localhost", "admin", "admin@123", "main");
    if($db->connect_error){
        echo "Failed";
    }
    else{
        echo "Success";
    }
?>

<!doctype html>
<html>
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capstone Project</title>

    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">

    <!-- Optional jQuery and Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
	<style>
		.carousel-item img {
    		max-height: 350px; /* Set your desired height */
    		object-fit: cover;
		}
		.carousel-caption-bg {
        background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
        padding: 10px;
        border-radius: 5px;
    }
</style>

</head>
<body>

<!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Capstone</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="#">Model</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="#">Graphs</a>
                </li>
            </ul>
        </div>
    </nav>

<!-- Carousel -->
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="crop1.jpg" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <div class="carousel-caption-bg">
                       	<h3>Team</h4>
                        <h4>Ektor Avlonitis</h4>
                        <h4>Alex Vavakas</h4>
                        <h4>Spyros Kalogeris</h4>
                        <h4>Pavlos</h4>
                    </div>
                </div>
            </div>
            <div class="carousel-item">
                <img src="crop2.jpg" class="d-block w-100" alt="...">
                <div class="carousel-caption d-none d-md-block">
                    <div class="carousel-caption-bg">
                        <h5>Helping the kids in need</h5>
                    </div>
                </div>
            </div>
            <!-- Add more carousel items here -->
        </div>
        <aclass="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
		<span class="carousel-control-prev-icon" aria-hidden="true"></span>
		<span class="sr-only">Previous</span>
		</a>
		<a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
		<span class="carousel-control-next-icon" aria-hidden="true"></span>
		<span class="sr-only">Next</span>
		</a>
		</div>

    
    <!-- Cards -->
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-4">
                <div class="card">
                    <img src="crop1.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">Card title 1</h5>
                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
	<div class="card">
	<img src="crop2.jpg" class="card-img-top" alt="...">
	<div class="card-body">
	<h5 class="card-title">Card title 2</h5>
	<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
	<a href="#" class="btn btn-primary">Go somewhere</a>
	</div>
	</div>
	</div>
	<div class="col-md-4">
	<div class="card">
	<img src="crop3.jpg" class="card-img-top" alt="...">
	<div class="card-body">
	<h5 class="card-title">Card title 3</h5>
	<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
	<a href="#" class="btn btn-primary">Go somewhere</a>
	</div>
	</div>
	</div>
	</div>
	</div>
</body>
</html>
