# Global Templates and Styling
At the root of the Django project, there is a `static` folder and a `templates` folder. These contain
the global template and styling that everything else in the app will inherit from.

To apply styling on an individual page or app, edit the `styles.css` in the individual app's static folder.

For example, on the homepage, there is going to be an announcement banner. All the styling should be done for it in the
css file at `core/static/styles.css`, or the even more specific `core/static/homepage/styles.css`. 

This isolates the styling to specific pages and components, which will make it easier to focus on elements towards
the end of the project.