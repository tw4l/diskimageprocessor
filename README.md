# CCA Disk Image Processor  

Analyze disk images and/or create ready-to-ingest SIPs from a directory of disk images and related files.  

**NOTE: This tool is in dev and should not be considered production-ready without testing**  
Version: 0.5.0 (alpha)

## Usage

Disk Image Processor has two modes: Analysis and Processing. Each mode can be run from the GUI interface or as a separate CLI utility by calling the underlying Python 3 script.  

### Analysis

Underlying script: `diskimageanalyzer.py`  

In Analysis mode, each disk image is scanned and reported on. When complete, an "analysis.csv" file is created containing the following information for each disk image:  

* Disk image name  
* File system  
* Date statement  
* Date begin  
* Date end  
* Extent  
* Virus found (Boolean value)  
* File formats  

The destination directory also contains a "reports" directory containing a sub-directory for each disk image scanned. Each of these disk image sub-directories contains:  

* A DFXML file  
* Text output from "disktype"  
* Brunnhilde reports (including logs and reports from clamAV and bulk_extractor)  

Because "Analysis" mode runs bulk_extractor against each disk, this process can take a while.  

*Note: For disks with NTFS, FAT, EXT, ISO9660, HFS+, UFS, RAW, SWAP, or YAFFS2 file systems, the dates reported by Brunnhilde and those reported in the DFXML/analysis CSV will likely differ. This is because tsk_recover is used to carve files from these disk images, and tsk_recover does not retain original file system dates. In these cases, the date stamps recorded in the DFXML file and reported in the analysis CSV should be considered the proper date values for the disk.*

### Processing

Underlying script: `diskimageprocessor.py`  

In Processing mode, each disk image is turned into a SIP, packaged as an ideal transfer to Archivematica's Automation tools, and reported on.

For disks with most file systems, `fiwalk` is used to generate DFXML and The Sleuth Kit's `tsk_recover` utility is used to carve allocated files from each disk image. Because tsk_recover does not retain file system timestamps, the program then rewrites the modified dates of files in the newly-created SIP based on the values recorded in the DFXML file.

For disks with an HFS file system, files are exported from the disk image using CLI version of HFSExplorer. For UDF disks, files are copied from the mounted disk image. For both HFS and UDF disks, the `walk_to_dfxml.py` script from DFXML Python bindings is used to generate DFXML.

When complete, a "description.csv" spreadsheet is created containing some pre-populated archival description:  
* Date statement  
* Date begin  
* Date end  
* Extent  
* Scope and content (containing information about the tool used to carve logical files and the most common file formats)

The destination directory also contains a log file and a "SIPs" directory containing a SIP created from each input disk image. 

Each SIP directory contains a metadata/checksum.md5 manifest by default, but may optionally be bagged instead. 

By default, the "objects" directory in each SIP contains both a copy of a raw disk image (regardless of whether the input was raw or E01) and logical files carved from the image by unhfs or a mount-and-copy routine, depending on the disk's file system. The user can choose to instead have SIPs include only logical files.

The "metadata/submissionDocumentation" directory in each SIP contains:  

* A DFXML file  
* Text output from "disktype"  
* Brunnhilde reports (including logs and reports from clamAV and, optionally, bulk_extractor)  

## Supported file systems

* NTFS  
* FAT  
* ext2/3  
* ISO9660  
* UDF
* HFS  
* HFS+  
* UFS  
* RAW  
* SWAP  
* YAFFS2  

## Supported disk image types  

* raw (dd, iso, img, etc.)  
* EnCase/EWF (E01)  

*Note: EnCase disk images are converted to raw disk images for processing using [libewf](https://github.com/libyal/libewf)'s `ewf_export` utility. In Processing mode, the converted raw image is retained in the SIP unless the user selects to retain only logical files.*

## Installation

This utility is designed for easy use in BitCurator v1.8.0+. It requires Python 2.7 (to run the GUI) and Python 3.4+ (to run the scripts that analyze and process disk images), both of which are already included in BitCurator.    

### Install as part of CCA Tools  

Install all of the CCA Tools (and PyQT4) together using the install bash script in the [CCA Tools repo](https://github.com/timothyryanwalsh/cca-tools).  

### Install as a separate utility
* Clone this repo to your local machine.  
* Make install script executable (may need to be run with sudo privileges):  
`chmod u+x install.sh` 
* Run the install script with sudo privileges:  
`sudo ./install.sh`  

## Credit  

Inspired by [Jess Whyte's work at the University of Toronto's Fisher Rare Book Library](https://saaers.wordpress.com/2016/04/12/clearing-the-digital-backlog-at-the-thomas-fisher-rare-book-library/comment-page-1/), especially the [Disk-ID-md5deep script](https://github.com/jesswhyte/Disk-ID-md5deep/).
