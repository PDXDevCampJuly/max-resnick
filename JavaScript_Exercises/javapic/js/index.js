/**
 * Created by Maxwell J. Resnick on 8/27/15.
 */

// We need to swap for the next image.

// We need to rotate every 20 secs.
function rotateAllTheThings() {
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
            jumbotron.style.backgroundImage = "url('" + rotatorImages[currentImageIndex] + "')";
        }
        // increase count
        currentImageIndex += 1;
    },3000);
}
// First we need to select some images of the 60
var rotatorImages = (function () {
   /*
    * rotatorImages
    * @returns [array] 6 image file paths
    * Use an IIFY for fun, and we only need this list once, per page load.
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

// Wait for our page to load, then kick of rotator.
window.addEventListener('load', rotateAllTheThings, false);


/*    function() {
    console.log("I am here.");
    this.rotateAllTheThings(e.target);
}, false);*/
