{
  description = "Scalpy Development Environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            python311
            python311Packages.pip
            python311Packages.virtualenv
            python311Packages.numpy
            python311Packages.scipy
          ];

          shellHook = ''
            echo "Scapy development environment activated"
            python -m venv .venv
            source .venv/bin/activate
            pip install scapy
	     
          '';
        };
      }
    );
}
