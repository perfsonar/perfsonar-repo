# perfSONAR Yum Repository RPM
This repository contains the files needed to build an RPM that configures yum to use the perfSONAR yum repository at http://software.internet2.edu/rpms/.

## Building the RPM

You may build the RPM by following the steps below (note these instructions assume you know the basics of building an RPM):

1. Build the source tarball:

    ```bash
    make dist
    ```
1. Copy the tarball and SPEC file to you RPM build directory:

    ```bash
    cp perfSONAR-repo.tar.gz ~/rpmbuild/SOURCES
    cp perfSONAR-repo.spec ~/rpmbuild/SPECS
    ```
1. Build the RPM:

    ```bash
    rpmbuild -ba SPEC/perfSONAR-repo.spec
    ```


*Note that to build the el5 version of this tool you need to build in an el5 environment. Likewise for el6. It is recommended you use a tool such as mock to accomplish this goal.*

