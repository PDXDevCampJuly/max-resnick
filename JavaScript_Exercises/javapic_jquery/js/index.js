/*
 * Javapic utilizing Jquery
 */


// Overkill for this assignment
var $jQ = jQuery.noConflict();
$jQ(document).ready(function(){

    // Our array of images.
    var rotatorImages = (function () {
       /*
        * rotatorImages
        * @description  First we need to select some images of the 60
        * @returns [array] 6 image file paths
        * Using an IIFY for fun but also we only need this list once, per page load.
        */
        this.randomImages = [];
        for (var i=0; i<7; i++) {
            this.filePrefix = "url(images/pdxcg_";
            this.filePostfix= ".jpg)";
            // we go up to 60, but add 1 in the end to account for 0.
            this.num = Math.floor(Math.random()*60) + 1;

            // we add a "0" but also just cast everything to string
            if (this.num < 10) {
                this.num = "0" + this.num.toString();
            } else {
                this.num = this.num.toString();
            }
            this.fullPath = this.filePrefix + this.num + this.filePostfix;
            this.randomImages.push(this.fullPath);
        }
        return this.randomImages;
    }());
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
            }, 5000);
    }());
});
