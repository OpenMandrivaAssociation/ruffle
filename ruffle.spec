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
cat >>.cargo/config <<EOF
[source."git+https://github.com/gfx-rs/wgpu?branch=v0.18"]
git = "https://github.com/gfx-rs/wgpu"
branch = "v0.18"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/egui?branch=consume_keys"]
git = "https://github.com/ruffle-rs/egui"
branch = "consume_keys"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/h263-rs?rev=16700664e2b3334f0a930f99af86011aebee14cc"]
git = "https://github.com/ruffle-rs/h263-rs"
rev = "16700664e2b3334f0a930f99af86011aebee14cc"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/jpegxr?branch=ruffle"]
git = "https://github.com/ruffle-rs/jpegxr"
branch = "ruffle"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/nellymoser?rev=4a33521c29a918950df8ae9fe07e527ac65553f5"]
git = "https://github.com/ruffle-rs/nellymoser"
rev = "4a33521c29a918950df8ae9fe07e527ac65553f5"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/nihav-vp6?rev=83c7e1094d603d9fc1212d39d99abb17f3a3226b"]
git = "https://github.com/ruffle-rs/nihav-vp6"
rev = "83c7e1094d603d9fc1212d39d99abb17f3a3226b"
replace-with = "vendored-sources"

[source."git+https://github.com/ruffle-rs/rust-flash-lso?rev=2f976fb15b30aa4c5cb398710dc5e31a21004e57"]
git = "https://github.com/ruffle-rs/rust-flash-lso"
rev = "2f976fb15b30aa4c5cb398710dc5e31a21004e57"
replace-with = "vendored-sources"
EOF


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
