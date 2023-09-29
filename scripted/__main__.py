import bs4
import pathlib


def extractFile(filename):
    
    with open(filename, encoding='utf-8') as infile:
        soup = bs4.BeautifulSoup(infile, "html.parser")
    srcs = soup.find_all('div', class_="transcript-row")
    ans = ""
    for x in srcs:
        txt = x.get_text(separator="/")
        txt = txt.split(sep="/")
        ans += txt[1]
        ans += " "
    return ans
    

def main():
    ans = extractFile("index.html")
    output = pathlib.Path("output.txt")
    output.touch()
    output.write_text(ans)
    return 0

if __name__ == "__main__":
    main()
