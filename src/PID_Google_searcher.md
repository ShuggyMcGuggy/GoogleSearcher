# PID Google Search application for news publishing
## Objective
Provide a daily serach on topics to enable a weekly selection to be 
published to linked in
Aggregate this and publish to a django website
Post entries to linked in to make the post

## Useful Resources
- [How to write google searches in python](https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4)
- [Django getting started](https://realpython.com/get-started-with-django-1/)
- [Django Job Aggregator](https://realpython.com/build-a-content-aggregator-python/)
- [Beautiful Soup web scraper](https://realpython.com/beautiful-soup-web-scraper-python/)
- [Markdown code syntax](https://daringfireball.net/projects/markdown/syntax#precode)

## Sat Nov 20 
Scrape a site: Betiful soup and site inspection
Start a Django project to enabel data presentatn and entry

### TODO Found the TODO facility in Pycharm
- include the tag TODO in the comment and it will be shown in the TODO list
- Lk this

<pre><code>
### Use of [] notation to pull dictionary entry from string

### How to activate a virtual environment from a bash shell
- [Link to answere](https://askubuntu.com/questions/813929/how-to-activate-a-virtualenv-within-bash-script-resulting-in-activated-prompt)

# Create temporary directory
TMPDIR="$(mktemp --directory)"
trap "echo 'INFO: Exited temporary shell.' >&2; rm --force --recursive '${TMPDIR}'" EXIT

# Set-up virtualenv in the temporary directory
virtualenv "${TMPDIR}"
. "${TMPDIR}/bin/activate"

# Install any required pip packages
[ -r "$(pwd)/pyReqs.txt" ] && pip install --requirement "$(pwd)/pyReqs.txt"

# Run a subshell with virtualenv already activated
bash --rcfile "${TMPDIR}/bin/activate" -i
</code></pre>