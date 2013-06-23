class python::pil {
  include python

  package { "libjpeg-dev":
    ensure => installed
  }

  file { "/usr/lib/libjpeg.so":
    ensure => "link",
    target => "/usr/lib/x86_64-linux-gnu/libjpeg.so",
    require => Package[ "libjpeg-dev" ]
  }

  package { [ "libfreetype6", "libfreetype6-dev" ]:
    ensure => installed
  }

  file { "/usr/lib/libfreetype.so":
    ensure => "link",
    target => "/usr/lib/x86_64-linux-gnu/libfreetype.so",
    require => Package[ "libfreetype6", "libfreetype6-dev" ]
  }

  package { "zlib1g-dev":
    ensure => installed
  }

  file { "/usr/lib/libz.so":
    ensure => "link",
    target => "/usr/lib/x86_64-linux-gnu/libz.so",
    require => Package[ "zlib1g-dev" ]
  }

  python::pip { "PIL":
    ensure => installed,
    require => Package[ "libjpeg-dev",
                        "libfreetype6",
                        "libfreetype6-dev",
                        "zlib1g-dev" ]
  }
}
