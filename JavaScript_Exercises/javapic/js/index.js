/**
 * Created by Maxwell J. Resnick on 8/27/15.
 * Spec
 * ====
 * index
 * -----
 * Load an assortment of images not all 60
 * image changes every 20 secs
 */

function rotateAllTheThings() {
    /*
     * rotateAllTheThings
     * @description changes the background on jumbotron every 20 secs.
     */
    var jumbotron = document.getElementById('jumbotron');
    var currentImageIndex = 0;
    // we use anon function to handle swapping images.
    setInterval(function () {
        if (currentImageIndex === 7) {
           /* we've reached the end, reset to the original image.
            * we set to "" because the image is really set in CSS, and we're
            * inline style.
            */
            jumbotron.style.backgroundImage = "";
            // reset counter
            currentImageIndex = 0;
        } else {
            // use our random list of images.
            jumbotron.style.backgroundImage = "url('" + rotatorImages[currentImageIndex] + "')";
        }
        // increase count
        currentImageIndex += 1;
    }, 20000); // Per spec need to rotate every 20 secs.
}

var rotatorImages = (function () {
   /*
    * rotatorImages
    * @description  First we need to select some images of the 60
    * @returns [array] 6 image file paths
    * Using an IIFY for fun but also we only need this list once, per page load.
    */
    this.randomImages = [];
    for (var i=0; i<7; i++) {
        this.filePrefix = "images/pdxcg_";
        this.filePostfix= ".jpg";
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

// Event Binding
window.addEventListener('load', rotateAllTheThings, false);
