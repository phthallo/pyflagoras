# Adding flags

To add a flag, you will need a `.svg` file of the flag's design. You can see some [here](https://commons.wikimedia.org/wiki/Category:SVG_flags_of_LGBT)! Furthermore, you will need to select the flag's **name**, **alias** and **ID**. For flags which have multiple designs, such as the multiple lesbian flags, please include a descriptor and/or year of release in the alias and ID to distinguish it from the other flags.

| Term | Definition | Example |
| ---- | ---------- | ------- |
| Name | The general name of the flag | Progress Pride |
| Alias | A unique, easier to type version of the flag's name | progresspride |
| ID | A unique identifier for the flag | progressPride_2018 | 

1. Fork the repository
2. Navigate to `src/pyflagoras/flags`
3. Create a new file called `<id>.json`
4. Fill the following `.json` out and paste it in the file, replacing the values as necessary.
    ```
    {
        "name": "<name>", 
        "id": "<id>", 
        "svg": "<yoursvgfile>"
    }
    ```
5. Navigate to `src/pyflagoras/flag_aliases.json` and add your flag alias and flag ID as a key-value pair. Please ensure that it fits alphabetically (just for stylistic purposes), and that the flag alias is in all-lowercase.
7. You're done! Open a new pull request to get your flag added.