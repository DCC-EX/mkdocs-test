#!/usr/bin/awk -f

function wrap_upper_parts(tag,    count, i, parts, out) {
    count = split(tag, parts, /_/)
    out = ""
    for (i = 1; i <= count; i++) {
        if (parts[i] ~ /^[A-Z0-9]+$/ && parts[i] ~ /[A-Z]/) {
            parts[i] = "9" parts[i] "9"
        }
        out = out (i == 1 ? "" : "_") parts[i]
    }
    return out
}

{
    # Match the pattern ZZ(something)   // comments
    if ($0 ~ /ZZ\([^)]*\)[[:space:]]*\/\/.*/) {
        # Extract "something" and "comments"
        match($0, /ZZ\(([^)]*)\)[[:space:]]*\/\/[[:space:]]*(.*)/, arr);
        something = arr[1];
        comments = arr[2];
        # Replace commas in "something" with spaces
        gsub(/,/, " ", something);
        linktag=arr[1]
        # Replace commas in "linktag" with underscores
        gsub(/,/, "_", linktag);
        # if linktag starts with '#' change it to ':h:'
        gsub(/#/, ":h:", linktag)
        # if linktag starts with '=' change it to ':e:'
        gsub(/=/, ":e:", linktag)
        # if linktag contains '^' change it to ':c:'
        gsub(/\^/, ":c:", linktag)
        # surround uppercase underscore-delimited parts with '9'
        linktag = wrap_upper_parts(linktag)
        
        # Print in the .md format used for mkdocs 
        printf "\n### [`<%s>`](?_%s)\n\n%s\n", something, linktag, comments;
    } 
}


# Copy any other lines starting with "///" removing the "///" prefix
/^[[:space:]]*\/\/\// {
    line = $0
    sub(/^[[:space:]]*\/\/\/[[:space:]]*/ , "" , line)
    print line
    next
}
