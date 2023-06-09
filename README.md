# queer-assistance-script-collection

Hey all! This repo was started as a way to make it easier for folk to submit erroneous concerns & complaints to the [Missouri Attorney General's form](https://ago.mo.gov/file-a-complaint/transgender-center-concerns), which is encouraging folk to report trans people and medical providers. This is scary because it makes it harder for folks to trust their neighbors, will potentially increase the risk of prosecution for medical providers who are providing care to trans kids and adults, and will cause a deterioration in the support networks of the LGBTQ+ community in Missouri.

To make use of the auto-generator, go check out the [website](https://pamplemoussecache.github.io/queer-assistance-script-collection/)!

## Notes for Contributers
#### Enable pre-commit hooks
These checks ensure that the code we merge in conforms to an opinionated style.
Running this `install` ensures that the checks will be run before your code
is pushed up to github.

```bash
pre-commit install --hook-type pre-push
```

If you ever want to run the checks ad-hoc, you can run `pre-commit run --all-files`.

Note that this is run as a Github Action each time your code is pushed.

#### Run the tests
To run the test suite, run this command in your Terminal from the root directory:

```bash
python -m unittest discover -s tests
```

Note that this is run as a Github Action each time your code is pushed.
