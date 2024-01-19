Name:           ruffle
Version:        20240119
Release:        1
Summary:        Adobe Flash Player emulator written in Rust
License:        Apache-2.0 OR MIT
URL:            https://ruffle.rs/
Source0:         https://github.com/ruffle-rs/ruffle/archive/refs/tags/ruffle-nightly-2024-01-19.tar.gz
Source1:        vendor.tar.xz
#Source2:        cargo_config

BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(x11)

%description
Ruffle is an Adobe Flash Player emulator written in the Rust programming
language. Ruffle targets both the desktop and the web using WebAssembly.

%prep
%autosetup -n %{name}-nightly-2024-01-19 -a1 -p1
%cargo_prep -v vendor

install -d -m 0755 .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."https://github.com/RustAudio/dasp"]
git = "https://github.com/RustAudio/dasp"
rev = "f05a703"
replace-with = "vendored-sources"

[source."https://github.com/ruffle-rs/gc-arena"]
git = "https://github.com/ruffle-rs/gc-arena"
replace-with = "vendored-sources"

[source."https://github.com/ruffle-rs/h263-rs"]
git = "https://github.com/ruffle-rs/h263-rs"
rev = "ce3d3c798190be1c78c47099e76d095756a195ac"
replace-with = "vendored-sources"

[source."https://github.com/ruffle-rs/nellymoser"]
git = "https://github.com/ruffle-rs/nellymoser"
replace-with = "vendored-sources"

[source."https://github.com/ruffle-rs/quick-xml"]
git = "https://github.com/ruffle-rs/quick-xml"
rev = "8496365ec1412eb5ba5de350937b6bce352fa0ba"
replace-with = "vendored-sources"

[source."https://github.com/ruffle-rs/rust-flash-lso"]
git = "https://github.com/ruffle-rs/rust-flash-lso"
rev = "19fecd07b9888c4bdaa66771c468095783b52bed"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
rm -f Cargo.lock

%build
%cargo_build

%install
#RUSTFLAGS=%%{rustflags} cargo install --root=%%{buildroot}%%{_prefix} --path .
# find out why this doesn't work
#%%cargo_install

install -Dm0755 target/release/ruffle_desktop %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
