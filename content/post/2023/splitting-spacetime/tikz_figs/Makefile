# Makefile to convert PDF to PNG and WebP

# List of PDF files to convert
PDF_FILES := K_volume_t.pdf K_volume_u.pdf

# Commands
CONVERT_PDF := convert -density 900
CWEBP := cwebp

# Targets
all: $(PDF_FILES:.pdf=.webp)

%.webp: %.png
	$(CWEBP) $< -o $@

%.png: %.pdf
	$(CONVERT_PDF) $< $@

clean:
	rm -f $(PDF_FILES:.pdf=.webp) $(PDF_FILES:.pdf=.png)

.PHONY: all clean
