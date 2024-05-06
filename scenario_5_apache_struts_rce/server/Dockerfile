# Start from the pre-existing Struts2 vulnerable image
FROM medicean/vulapps:s_struts2_s2-053

# Manually specify the kubectl version to use
ENV KUBECTL_VERSION="v1.20.0"

# Add the kubectl binary directly from the Kubernetes release page
ADD https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl /usr/local/bin/kubectl

# Make kubectl executable
RUN chmod +x /usr/local/bin/kubectl

# Verify kubectl is installed
RUN /usr/local/bin/kubectl version --client

