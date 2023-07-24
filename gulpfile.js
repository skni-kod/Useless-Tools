const { src, dest, series, parallel, watch} = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const cssnano = require('gulp-cssnano');
const autoprefixer = require('gulp-autoprefixer');
const rename = require('gulp-rename');
const babel = require('gulp-babel');
const uglify = require('gulp-uglify');
const imagemin = require('gulp-imagemin');
const sourcemaps = require('gulp-sourcemaps');
const browserSync = require('browser-sync').create();
const clean = require('gulp-clean');
const shell = require('gulp-shell');

const reload = browserSync.reload;

const paths = {
    sass: './src/sass/**/*.scss',
    js: './src/js/**/*.js',
    img: './src/img/*',

    dist: './static',
    html: './core/templates/**/*.html',

    sassDest: './static/css',
    jsDest: './static/js',
    imgDest: './static/img'
}

function sassCompiler(done){
    src(paths.sass)
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(cssnano())
        .pipe(rename( {suffix: '.min'} ))
        .pipe(sourcemaps.write())
        .pipe(dest(paths.sassDest))
    done()
}

function javaScript(done) {
    src(paths.js)
        .pipe(sourcemaps.init())
        .pipe(babel({
            presets: ['@babel/env']
        }))
        .pipe(uglify())
        .pipe(rename( {suffix: '.min'} ))
        .pipe(sourcemaps.write())
        .pipe(dest(paths.jsDest))
    done()
}

function convertImage(done) {
    src(paths.img)
        .pipe(imagemin())
        .pipe(dest(paths.imgDest))
    done()
}

function startBrowserSync(done){
    browserSync.init({
        proxy: 'http://127.0.0.1:8000/'
    });
    done()
}

function watchForChanges(done){
    watch([paths.html, paths.js, paths.sass], parallel(sassCompiler, javaScript)).on("change", reload)
    watch(paths.img, convertImage).on("change", reload)
    done()
}

function cleanStuff(done){
    src(paths.dist, {read: false})
        .pipe(clean())
    done()
}

function runServer(done){
    console.log('running server');
    shell.task('python manage.py runserver')
    done()
}

const mainFunctions = parallel(sassCompiler, javaScript, convertImage)

exports.cleanStuff = cleanStuff //      gulp cleanStuff, jak chcecie wyczyscic static
exports.default = series(runServer, mainFunctions, startBrowserSync, watchForChanges)