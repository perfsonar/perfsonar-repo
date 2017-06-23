PACKAGE=perfSONAR-repo

dist:
	mkdir /tmp/$(PACKAGE)
	tar ch -T MANIFEST | tar x -C /tmp/$(PACKAGE)
	tar czf $(PACKAGE).tar.gz -C /tmp $(PACKAGE)
	rm -rf /tmp/$(PACKAGE)

