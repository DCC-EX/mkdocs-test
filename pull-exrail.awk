# Print lines that start with optional whitespace followed by "#define"
# Usage: awk -f pull-exrail.awk inputfile > outputfile
/^[[:space:]]*#define/ {
    line = $0
    sub(/^[[:space:]]*#define[[:space:]]*/ , "" , line)
    # print "\n## " line "\n"
    search_term = line
    sub(/\(.*/, "", search_term)
    sub(/[[:space:]]+$/, "", search_term)
    print "\n## [" escape_markdown(line) "](?" url_encode(search_term) ")\n"
    next
}

function escape_markdown(text,    result, i, character) {
    result = ""
    for (i = 1; i <= length(text); i++) {
        character = substr(text, i, 1)
        if (character == "\\" || character == "[" || character == "]") {
            result = result "\\"
        }
        result = result character
    }
    return result
}

function url_encode(text,    result, i, character, code, printable) {
    result = ""
    printable = ""
    for (code = 32; code <= 126; code++) {
        printable = printable sprintf("%c", code)
    }

    for (i = 1; i <= length(text); i++) {
        character = substr(text, i, 1)
        if (character ~ /^[[:alnum:]_.~-]$/) {
            result = result character
        } else {
            code = index(printable, character)
            if (code) {
                result = result "%" sprintf("%02X", code + 31)
            } else {
                result = result character
            }
        }
    }
    return result
}



# Match lines starting with optional space then "///brief" and remove the prefix
/^[[:space:]]*\/\/\/brief/ {
    line = $0
    sub(/^[[:space:]]*\/\/\/brief[[:space:]]*/ , "" , line)
    print line
    print ""
    next
}
# Match lines starting with optional space then "///param" and remove the prefix
/^[[:space:]]*\/\/\/param/ {
    line = $0
    sub(/^[[:space:]]*\/\/\/param[[:space:]]*/ , "- " , line)
    print line
    next
}


# Copy any other lines starting with "///" removing the "///" prefix
/^[[:space:]]*\/\/\// {
    line = $0
    sub(/^[[:space:]]*\/\/\/[[:space:]]*/ , "" , line)
    print line
    print ""
    next
}

