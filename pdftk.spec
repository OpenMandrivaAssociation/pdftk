%define gcj_support 1
Name:		pdftk
Version:	1.44
Release:	4
Summary:	PDF Tool Kit
License:	GPLv2+
Group:		Publishing
URL:		http://www.pdfhacks.com/pdftk/
Source0:	http://www.pdfhacks.com/pdftk/%{name}-%{version}-src.zip
Patch0:		pdftk-1.44-makefile-fix.patch
BuildRequires:	gcc-java
BuildRequires:	libgcj-devel
BuildRequires:	unzip
BuildRequires:	fastjar
BuildRequires:	dos2unix
Requires:	bouncycastle

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
%setup -q -n %{name}-%{version}-dist
%patch0 -p0 -b .makefix

%{__perl} -pi -e "s/\r$//g" pdftk.1.txt

%{__rm} -r java/gnu_local java/java_local
dos2unix changelog.txt

%build
pushd pdftk
GCJFLAGS="%{optflags} -I`pwd`/../java -Wno-all" %{__make} -f Makefile.Redhat
popd

%install
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -a pdftk/pdftk %{buildroot}%{_bindir}/pdftk

%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__cp} -a pdftk.1 %{buildroot}%{_mandir}/man1/pdftk.1

%files
%defattr(0644,root,root,0755)
%doc pdftk.1.html pdftk.1.txt changelog.txt
%attr(0755,root,root) %{_bindir}/pdftk
%{_mandir}/man1/pdftk.1*


%changelog
* Sun Dec 19 2010 Tomas Kindl <supp@mandriva.org> 1.44-3mdv2011.0
+ Revision: 623103
- update for GCC 4.5
- fix buildrequires
- update to 1.44, drop unneeded patches

* Wed Aug 25 2010 Funda Wang <fwang@mandriva.org> 1.41-10mdv2011.0
+ Revision: 573211
- rebuild for new gcc

* Tue Oct 20 2009 Ahmad Samir <ahmadsamir@mandriva.org> 1.41-9mdv2010.0
+ Revision: 458430
- Add bouncycastle as BR (fix bug #54738)

* Sat Sep 26 2009 Michael Scherer <misc@mandriva.org> 1.41-8mdv2010.0
+ Revision: 449472
- rebuild for bug 48880
- fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + David Walluck <walluck@mandriva.org>
    - clean up build
    - BuildRequires: java-devel-gcj
    - fix build
    - bump release for build system bug
    - change BuildRequires
    - fix BuildRequires
    - fix URL and Source0 URL
    - patch for new gcj

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.41-3mdv2008.1
+ Revision: 136654
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Pascal Terjan <pterjan@mandriva.org> 1.41-3mdv2008.0
+ Revision: 83393
- and make it buildable too
- Make the package submitable
- rebuild
- rebuild


* Tue Dec 19 2006 Lev Givon <lev@mandriva.org> 1.41-1mdv2007.0
+ Revision: 100300
- Import pdftk

