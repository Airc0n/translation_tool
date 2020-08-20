# Translation Tool


## Purpose

Build up a tool for frontend developer to create new template and default resource and generate a default html.
Content maintainer could use this tool to modify resource and generate others html.                                              
       
## API

### /v1/translation/templates/
`GET`  List all templates

`example`
http://localhost:8000/api/v1/translation/templates/

### /v1/translation/resources/
`GET`  List all belong the html template resources
 
`Parameter`
- tid: (int) => the html_template id

`example`
http://localhost:8000/api/v1/translation/resources/?tid=1  