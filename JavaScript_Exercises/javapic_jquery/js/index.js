/*
 * Javapic utilizing Jquery
 */

var rotatorImages = new javapicImages(true).randomImages;

$jQ(document).ready(function () {
    console.log(javapicImages.allImages);
    // Our array of images.
    (function () {
        this.$origJummbotronImage = $jQ('#jumbotron').css('background-image');
        var $jumbotron = $jQ('#jumbotron');
        rotatorImages.push($origJummbotronImage);
        var currentImageIndex = 0;
        setInterval(function() {
            if (currentImageIndex > rotatorImages.length) {
                // reset counter
                currentImageIndex = 0;
            }
            // change image
            $jumbotron.css('background-image', rotatorImages[currentImageIndex]);
            // increase count
            currentImageIndex += 1;
            }, 20000);
    }());
});
