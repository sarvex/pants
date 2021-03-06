# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

# This BUILD file defines common external library dependencies used across many modules.  Modules
# can use these jar_library deps by specifying '3rdparty:[name]' in their dependencies list.

# To add dependency for a JVM-tool needed by Pants itself (e.g., Antlr),
# see http://pantsbuild.github.io/dev_tasks.html#jvm-tool-bootstrapping

###################
# Production libs
#

def add_log4j_excludes(jar):
  return (jar.exclude(org='jline', name='jline')
            .exclude(org='javax.jms', name='jms')
            .exclude(org='com.sun.jdmk', name='jmxtools')
            .exclude(org='com.sun.jmx', name='jmxri'))

jar_library(name='checkstyle',
            jars = [
              jar(org='com.puppycrawl.tools', name='checkstyle', rev='5.5')
                .exclude(org='com.google.collections', name='google-collections')
                .with_sources(),
            ],
            dependencies = [
              # Needs this as the replacement for the excluded google-collections.
              ':guava',
            ],
           )

jar_library(name='commons-lang',
            jars = [
              jar(org='commons-lang', name='commons-lang', rev='2.5').with_sources()
            ]
           )


jar_library(name='cucumber-java',
            jars=[
              jar(org='info.cukes', name='cucumber-java', rev='1.1.7'),
            ],
)

# common rev for all com.twitter%finagle* artifacts
FINAGLE_REV = '6.8.1'

jar_library(name='finagle-core',
            jars = [
              jar(org='com.twitter', name='finagle-core_2.9.2', rev=FINAGLE_REV)
                .with_sources(),
            ],
            dependencies = [
              ':util-core'
            ])

jar_library(name='finagle-thrift',
            jars = [
              jar(org='com.twitter', name='finagle-thrift_2.9.2', rev=FINAGLE_REV)
            ])

# common rev for all com.google.guava%guava* artifacts
GUAVA_REV = '16.0'

jar_library(name='guava',
            jars = [
              jar(
                org='com.google.guava', name='guava', rev=GUAVA_REV,
                apidocs='http://docs.guava-libraries.googlecode.com/git-history/'
                          '%s/javadoc/' % GUAVA_REV
              ).with_sources().with_docs(),

              # Defined in provided scope so we provide here
              jar(org='javax.inject', name='javax.inject', rev='1').with_sources(),
            ],
            dependencies = [
              ':jsr305',
            ],
           )

jar_library(name='jsr305',
            jars = [
              jar(org='com.google.code.findbugs', name='jsr305', rev='1.3.9')
            ]
           )

jar_library(name='log4j',
            jars = [
              add_log4j_excludes(jar(org='log4j', name='log4j', rev='1.2.15').with_sources())
            ])

jar_library(name='protobuf-2.4.1',
            jars = [
              jar(org='com.google.protobuf', name='protobuf-java', rev='2.4.1').with_sources()
            ]
           )

jar_library(name='protobuf-java',
            dependencies = [
              ':protobuf-2.4.1'
            ])

jar_library(name='protobuf-test-import',
  jars = [
    jar(org='com.squareup.testing.protolib', name='protolib-test', rev='1.0.1'),
  ],
)

jar_library(name='scala-compiler',
            jars = [
              jar(org='org.scala-lang', name='scala-compiler', rev='2.9.3').with_sources()
            ]
           )

jar_library(name='scala-library',
            jars = [
              jar(org='org.scala-lang', name='scala-library', rev='2.9.3').with_sources()
            ]
           )

jar_library(name='scrooge-core',
            jars = [
              # used by scrooge-generator in BUILD.tools:scrooge-gen
              jar(org='com.twitter', name='scrooge-core_2.9.2', rev='3.12.1').with_sources()
            ]
          )

jar_library(name='shapeless',
            jars=[
              jar(org='com.chuusai', name='shapeless_2.9.2', rev='1.2.4'),
            ],
)

jar_library(name='slf4j-api',
            jars = [
              jar(org='org.slf4j', name='slf4j-api', rev='1.6.1').with_sources()
            ]
)

jar_library(name='libthrift-0.5.0',
            jars = [
              jar(org='org.apache.thrift', name='libthrift', rev='0.5.0-1'),
            ]
           )

jar_library(name='thrift-0.5.0',
            dependencies = [
              ':commons-lang',
              ':libthrift-0.5.0',
              ':slf4j-api',
            ]
           )

jar_library(name='thrift-0.5.0-finagle',
            dependencies = [
              ':thrift-0.5.0',

              # finagle thrift extra deps
              ':finagle-core',
              ':finagle-thrift',
              ':util-core',
            ]
           )

jar_library(name='thrift',
            dependencies = [ ':thrift-0.5.0' ])

# common rev for all com.twitter%util* artifacts
UTIL_REV = '6.8.1'

jar_library(name='util-core',
            jars = [
		    jar(org='com.twitter', name='util-core_2.9.2', rev=UTIL_REV).with_sources() ])


###############
# Test support
#

jar_library(name='hamcrest-core',
            jars = [ jar(org='org.hamcrest', name='hamcrest-core', rev='1.3') ])

jar_library(name='junit',
            jars = [
              jar(org='junit', name='junit-dep', rev='4.11').with_sources(),
            ],
            dependencies = [
              ':hamcrest-core',
            ],
           )

jar_library(name='specs_2.9',
            jars = [
              jar(org='org.scala-tools.testing', name='specs_2.9.3', rev='1.6.9')
            ]
           )

jar_library(name='specs', dependencies = [ ':specs_2.9' ])
