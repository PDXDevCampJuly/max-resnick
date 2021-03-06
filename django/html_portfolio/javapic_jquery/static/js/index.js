/*
 * Javapic utilizing Jquery
 */

var rotatorImages = new javapicImages(true).randomImages;

$jQ(document).ready(function () {
/*
 * @description wait until the page loads to start rotation.
 */
(function () {
    /*
     * @description rotate all the things.
     */
    var $jumbotron = $jQ('#jumbotron');
    this.$origJummbotronImage = $jumbotron.css('background-image');
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
