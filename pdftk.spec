%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Name:		pdftk
Version:	2.02
Release:	1
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		http://www.pdfhacks.com/pdftk/
Source0:	%{name}-%{version}-x64.tar.xz
Source1:	%{name}-%{version}-x32.tar.xz

Requires:	bouncycastle
Requires:   libgcj.so.14%{_arch_tag_suffix}


%description
Pdftk is a simple tool for doing everyday things with PDF documents.
Keep one in the top drawer of your desktop and use it to:
- Merge PDF Documents
- Split PDF Pages into a New Document
- Decrypt Input as Necessary (Password Required)
- Encrypt Output as Desired
- Fill PDF Forms with FDF Data and/or Flatten Forms
- Apply a Background Watermark
- Report on PDF Metrics, including Metadata and Bookmarks
- Update PDF Metadata
- Attach Files to PDF Pages or the PDF Document
- Unpack PDF Attachments
- Burst a PDF Document into Single Pages
- Uncompress and Re-Compress Page Streams
- Repair Corrupted PDF (Where Possible)

%prep
%setup -c -T
%ifarch x86_64
tar -xf %{SOURCE0}
%else
tar -xf %{SOURCE1}
%endif

%build

%install
cp -R /usr %{buildroot}/

%files
%doc copyright changelog* NEWS*
%{_bindir}/pdftk
%{_mandir}/man1/pdftk.1*
