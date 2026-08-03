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

function sort_blocks(    i, j, tmp_key, tmp_value) {
    for (i = 2; i <= block_count; i++) {
        tmp_key = block_sort_key[i]
        tmp_value = block_content[i]
        j = i - 1
        while (j >= 1 && block_sort_key[j] > tmp_key) {
            block_sort_key[j + 1] = block_sort_key[j]
            block_content[j + 1] = block_content[j]
            j--
        }
        block_sort_key[j + 1] = tmp_key
        block_content[j + 1] = tmp_value
    }
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
        
        block_count++
        current_block = block_count
        block_sort_key[current_block] = tolower(something) "\034" linktag
        block_content[current_block] = "\n### [`<" something "`>](?_" linktag ")\n\n" comments "\n"

    } 
}

# Copy any other lines starting with "///" removing the "///" prefix
/^[[:space:]]*\/\/\// {
    line = $0
    sub(/^[[:space:]]*\/\/\/[[:space:]]*/ , "" , line)
    if (current_block > 0) {
        block_content[current_block] = block_content[current_block] line "\n"
    } else {
        standalone_lines = standalone_lines line "\n"
    }
    next
}

END {
    sort_blocks()

    if (standalone_lines != "") {
        printf "%s", standalone_lines
    }

    for (i = 1; i <= block_count; i++) {
        printf "%s", block_content[i]
    }
}
