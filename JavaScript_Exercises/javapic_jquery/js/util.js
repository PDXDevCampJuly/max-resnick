/**
 * Created by Maxwell J. Resnick on 9/1/15.
 */
function javapicImages () {
       /*
        * javapicImages
        * @description  First we need to select some images of the 60
        * @returns [array] 6 image file paths
        * Using an IIFY for fun but also we only need this list once, per page load.
        */
        var filePrefix = "url(images/pdxcg_";
        var filePostfix = ".jpg)";
        this.randomImages = (function () {
            this._randomImages = [];
            for (var i = 0; i < 7; i++) {
                // we go up to 60, but add 1 in the end to account for 0.
                this.num = Math.floor(Math.random() * 60) + 1;
                // we add a "0" but also just cast everything to string
                if (this.num < 10) {
                    this.num = "0" + this.num.toString();
                } else {
                    this.num = this.num.toString();
                }
                this.fullPath = filePrefix + this.num + filePostfix;
                this._randomImages.push(this.fullPath);
            }
            return this._randomImages;
        }());
        this.allImages = (function() {
                this.images = [];
                for (var i = 0; i < 60; i++) {
                    this.num = i+1;
                    // we add a "0" but also just cast everything to string
                    if (this.num < 10) {
                        this.num = "0" + this.num.toString();
                    } else {
                        this.num = this.num.toString();
                    }
                    this.fullPath = this.filePrefix + this.num + this.filePostfix;
                    this.images.push(this.fullPath);
                    }
                    return this.images;
        }());
};