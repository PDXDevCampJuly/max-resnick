/**
 * Created by Maxwell J. Resnick on 8/27/15.
 */



// First we need to select some images of the 60

// We need to paint the page with the images

// We need to rotate.

// Use an IIFY for fun, and we only need this list once.



var rotatorImages = (function () {
   /*
    * rotatorImages - an array of 6 image files
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
